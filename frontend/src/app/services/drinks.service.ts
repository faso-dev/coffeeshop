import {Injectable} from '@angular/core';
import {HttpClient, HttpHeaders} from '@angular/common/http';

import {AuthService} from './auth.service';
import {environment} from 'src/environments/environment';

export interface Drink {
    id: number;
    title: string;
    recipe: Array<{
        name: string,
        color: string,
        parts: number
    }>;
}

export type Violation = {
    [key: string]: {
        errors: Array<string>
    }
}

@Injectable({
    providedIn: 'root'
})
export class DrinksService {

    url = environment.apiServerUrl;

    public items: { [key: number]: Drink } = {};


    constructor(private auth: AuthService, private http: HttpClient) {

    }


    getHeaders() {
        return {
            headers: new HttpHeaders()
                .set('Authorization', `Bearer ${this.auth.activeJWT()}`)
        };
    }

    getDrinks() {
        if (this.auth.can('get:drinks-detail')) {
            this.http.get(this.url + '/drinks-detail', this.getHeaders())
                .subscribe((res: any) => {
                    this.drinksToItems(res.drinks);
                    console.log(res);
                });
        } else {
            this.http.get(this.url + '/drinks', this.getHeaders())
                .subscribe((res: any) => {
                    this.drinksToItems(res.drinks);
                    console.log(res);
                });
        }

    }

    saveDrink(drink: Drink, onSuccess: () => void, onError: (violations: Violation) => void) {
        if (drink.id >= 0) { // patch
            this.http.patch(this.url + '/drinks/' + drink.id, drink, this.getHeaders())
                .subscribe((res: any) => {
                    if (res.success) {
                        this.addDrink(res.drink);
                        onSuccess()
                    }
                }, (err: any) => {
                    if (err.status === 422) {
                        onError(err.error.violations);
                    }
                    console.log(err);
                });
        } else { // insert
            this.http.post(this.url + '/drinks', drink, this.getHeaders())
                .subscribe((res: any) => {
                    if (res.success) {
                        this.addDrink(res.drink);
                        onSuccess()
                    }
                }, (err: any) => {
                    if (err.status === 422) {
                        onError(err.error.violations);
                    }
                    console.log(err);
                });
        }

    }

    deleteDrink(drink: Drink) {
        delete this.items[drink.id];
        this.http.delete(this.url + '/drinks/' + drink.id, this.getHeaders())
            .subscribe((res: any) => {

            });
    }

    addDrink(drink: Drink) {
        this.items[drink.id] = drink;
    }

    drinksToItems(drinks: Array<Drink>) {
        for (const drink of drinks) {
            this.items[drink.id] = drink;
        }
    }

}
