# Week 5 Assignment

## Getting Started

**Before setting up your repo, note that this assignment has a couple different options. Please read through each option before setting up your app, because it may affect what you name the app.**

1. Fork this repository and clone the code to your machine.
2. Setup your application with `create-react-app`
3. Ensure you can run your dev server

## Overview

For this assignment, you'll be creating an app to view a collection of fictional characters.

You may choose from one of the following APIs.

* [Star Wars API](https://swapi.co/)
* [Pokemon API](https://pokeapi.co/)
* [Rick and Morty API](https://rickandmortyapi.com/)

Please note that these APIs will rate-limit you. Read the documentation and be aware of the rate-limiting enabled on each API. If you find yourself calling the API too many times, look into downloading an example response and use that while building out your app.

### Requirements

For this UI, you'll want an app that has two pages:

* The home page, for displaying a list of characters from your API
    * Each character component should contain a link to a character detail page
    * The name of the character is required. Anything else (character image, short description) is optional
* A character detail page, for displaying a specific character's information
    * Should display at least 4-5 facts about the character
    * Should display the character image if returned from the API. If not returned from the API, it is optional. However, you could find images on Google to map to the character.

Additional requirements:

* Uses React Router to switch between pages
* Uses route params to pass the character ID to the character detail page
* Uses `fetch` to retrieve the list of characters and the character details
* Uses React components that...
    * Are modular/reusable.
    * Are tested with at least one snapshot test per component.
    * Use the appropriate loops/conditionals to map and display components.
    * Use propTypes to define props.
* Styled with CSS to look decent

Note that these are the only requirements. The APIs may have paging for getting all the characters. You don't need to implement that (although you're free to if you wish).

### Inspiration

* [Google results for Star Wars characters](https://www.google.com/search?q=list+of+star+wars+characters)
* [Giant Bomb original 150 Pokemon](https://www.giantbomb.com/profile/wakka/lists/the-150-original-pokemon/59579/)

## Submission

1. In order for a valid submission, your app should run and display a UI when running `npm start`.
2. Create a pull request to this repository. There will be no CI.

## Extras (optional)

* Enable paging for the character list (if supported by the API)
* Incorporate more pages using other features of your API
* Add a search box feature to the character home page to filter the character list
* Add the ability to "favorite" a character and store favorite characters using the browser's `localStorage` API