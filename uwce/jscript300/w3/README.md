# Assignment 3

## Getting Started

1. Fork this repository and clone the code to your machine.
2. Setup your application
   ```bash
   # Make sure you run this command inside the week3 folder. Check via `pwd`
   # Not doing so may cause the create-react-app command to fail
   pwd
   # /path/to/week3
   create-react-app ecommerce-ui
   ```
3. Ensure you can run your dev server
   ```bash
   cd ecommerce-ui
   npm start

   # or if you're using yarn
   cd ecommerce-ui
   yarn start
   ```

## Overview

For this assignment, you'll be creating an e-commerce UI using React.

Why e-commerce? E-commerce drives a major portion of the web. People buy physical products via e-commerce (Amazon, Nordstrom, Zulily). Software services (TurboTax) and nonprofits (Washington Trails Association) also make up the e-commerce portion of the web.

E-commerce allows companies to cater to a national/global audience. It's also a game-changer for individuals because it lowers barriers to entry for online sales.

### Requirements

For this UI, we'll be using some fake data that represents a collection of vacation rentals (Airbnb-like). Additionally, the UI appearance will mostly be up to you, although you're free to use other websites and designs as inspiration.

Ensure that your UI meets the following criteria:

* Renders the provided data using React components
    * Data: <https://github.com/modern-web-application-uw18/react-airbnb-data>
    * Copy the JSON files to your project and import them into a component like so:
      ```js
      import airbnbs from './airbnbs.json';
      ```
    * At minimum, your UI should display the title, image, and payment information
* Uses React components that...
    * Are modular/reusable. For example, each vacation rental could be considered a modular and reusable component.
    * Are tested with at least one snapshot test per component.
    * Use the appropriate loops/conditionals to map and display components.
    * Use propTypes to define props.
* Offers a "Shopping Cart" functionality where you can add a vacation rental to a shopping cart. This shopping cart should...
    * Be displayed above the vacation rentals
    * Allow the user to remove a vacation rental from the cart if they change their mind
    * Display the total payment due based on the vacation rentals in the cart
* In order to facilitate the "Shopping Cart" functionality, each vacation rental should have a button that allows the user to add a vacation rental to the shopping cart.

### Inspiration

* [Airbnb](https://www.airbnb.com/)
* [Nike](https://store.nike.com/us/en_us/)
* [REI](https://www.rei.com/)

## Submission

1. In order for a valid submission, your app should run and display a UI when running `npm start`.
2. Create a pull request to this repository. There will be no CI.

## Extras

* Make the shopping cart hideable/showable, in order to avoid clutter. This could be implemented as a hide/show button.
* Create a UI that allows the user to enter their own vacation rentals. This should...
    * Allow the user to view a form
    * Allow the user to enter vacation rental information, such as the title, image, price, etc.
    * Add the new rental to the list of vacation rentals being displayed