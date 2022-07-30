# Coffee Shop Frontend

## Getting Setup

> _tip_: this frontend is designed to work with [Flask-based Backend](../backend). It is recommended you stand up the
> backend first, test using Postman, and then the frontend should integrate smoothly.

### Installing Dependencies

#### Installing Node and NPM

This project depends on Nodejs and Node Package Manager (NPM). Before continuing, you must download and install Node (
the download includes NPM) from [https://nodejs.com/en/download](https://nodejs.org/en/download/).

#### Installing Ionic Cli

The Ionic Command Line Interface is required to serve and build the frontend. Instructions for installing the CLI is in
the [Ionic Framework Docs](https://ionicframework.com/docs/installation/cli).

#### Installing project dependencies

This project uses NPM to manage software dependencies. NPM Relies on the package.json file located in the `frontend`
directory of this repository. After cloning, open your terminal and run:

> _tip_: Be sure to have node 10.9.0 installed. You can have this version with nvm `nvm install 10.9.0`
> . [NVM WEBSITE](https://nvm.io/en/download.html).
> _tip_: Be sure to have the 6.2.0 version of npm.
> _tip_: Be sure to have the ionic CLI installed. You can have it with `npm install -g @ionic/cli`.

```bash
npm install
```

> _tip_: **npm i** is shorthand for **npm install**

## Required Tasks

Before to run the frontend, be sure to run the backend first.

## Running Your Frontend in Dev Mode

With ionic, you can run your frontend in dev mode. To do so, run the following command:

```bash
ionic serve
```

## Stand outing the Frontend

- I add some extra features to the frontend to handle drink creation validation and display violations errors returned
  by the backend.

You can find the code in the `src/app/services/drinks.service.ts` file. These features are implemented in
the `saveDrink` method.

- In the drink form component, I juste add the needed callbacks to the saveDrink method to handle validation errors and
  alert them.

You can find the code in the `src/app/components/drink-menu/drink-form/drink-form.component.ts` file.

- I also fix some bug in the drink service. So after a creation of a drink, we'll add this drink to the list of drinks
  instead of replacing it(list).

Also take not that a post verb to create resource doesn't return a list of resources but the resource itself.

You can find the code in the `src/app/services/drinks.service.ts` file on the method `addDrink`.


### Resources

[Ionic CLI](https://ionicframework.com/docs/cli)
[Angular 7 Docs](https://v7.angular.io/docs)
[Flask Generic Exception Handler](https://flask.palletsprojects.com/en/2.1.x/errorhandling/#generic-exception-handlers)


