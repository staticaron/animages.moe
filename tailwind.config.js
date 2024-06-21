/** @type {import('tailwindcss').Config} */

const path = require('path');

module.exports = {
  content: ["templates/*"],
  theme: {
    extend: {
      backgroundImage : {
        'anime-background' : "url('/static/images/laevateinn/collection1/art1.png')",
      }, 
      fontFamily : {
        'trashhand' : ['TrashHand'],
        'playtime' : ['PlayTime']
      }
    },
  },
  plugins: [
    function({ addBase }) {
      addBase({
        '@font-face': {
          fontFamily: 'TrashHand',
          src: "url('/static/fonts/TrashHand.ttf')",
          fontWeight: 'normal',
          fontStyle: 'normal',
        },
      });
    },
    function({ addBase }) {
      addBase({
        '@font-face': {
          fontFamily: 'PlayTime',
          src: "url('/static/fonts/playtime.ttf')",
          fontWeight: 'normal',
          fontStyle: 'normal',
        },
      });
    },
  ],
}

