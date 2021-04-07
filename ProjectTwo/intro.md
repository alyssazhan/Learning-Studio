## Learning React

Become fluent in the toolchain supporting React, including NPM, Webpack, Babel, and ES6/ES2015 Javascript syntax.

### Mar 3

Collecting learning resources and making a plan for the project.

- Tutorial: [https://reactjs.org/tutorial/tutorial.html](https://reactjs.org/tutorial/tutorial.html)
- Course: [https://www.udemy.com/course/react-redux/](https://www.udemy.com/course/react-redux/)

### Mar 10

Setup for the Tutorial

There are two ways to complete this tutorial: write the code in the browser, or set up a local development environment on my computer.I'll do it on the browser.

- Write Code in the Browser 
  
Here's the code: [https://codepen.io/ali_zhan/pen/yLVGNMR](https://codepen.io/ali_zhan/pen/yLVGNMR)

### Mar 24

- Inspecting the Starter Code
- Passing Data Through Props. I’ve “passed a prop” from a parent Board component to a child Square component.
- Making an Interactive Component. I filled the Square component with an “X” when we click it.

Here's the code: [https://codepen.io/ali_zhan/pen/ExZVxyx](https://codepen.io/ali_zhan/pen/ExZVxyx)

### Mar 31

Completing the Game

- Lifting State Up. Now the state is stored in the Board component instead of the individual Square components. When the Board’s state changes, the Square components re-render automatically.
- Function Components. It's a simpler way to write components that only contain a render method and don’t have their own state.
- Declaring a Winner. I added helper function to show when the game is won and there are no more turns to make.

Here's the code: [https://codepen.io/ali_zhan/pen/BappdLK](https://codepen.io/ali_zhan/pen/BappdLK)

### Apr 7

Adding Time Travel

- Storing a History of Moves. I stored the past squares arrays in another array called history. The history array represents all board states, from the first to the last move,
- Lifting State Up, Again. I had the Board component receive squares and onClick props from the Game component.
- Picking a Key. Key is a special and reserved property in React.
- Implementing Time Travel. If player clicks on any step in the game’s history, the tic-tac-toe board should immediately update to show what the board looked like after that step occurred.

Here's the code: [https://codepen.io/ali_zhan/pen/YzNreBb](https://codepen.io/ali_zhan/pen/YzNreBb)