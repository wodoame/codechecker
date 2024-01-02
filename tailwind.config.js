/** @type {import('tailwindcss').Config} */
module.exports = {
  prefix:'tw-',
  important:true, 
  content: ["./codechecker/templates/**/*.html"],
  theme: {
    extend: {
      colors:{
        // 'proj-white':'#F0F0F0', 
        'proj-white':'#F9F9F9', 
        'proj-blue':'#0B409C', 
        'proj-navy':'#10316B', 
        'proj-yellow':'#FDBE34', 
        'proj-active':'#E7EFFF'
      }
    },
  },
  plugins: [],
}

/*
npx tailwindcss -i ./dist/input.css -o ./codechecker/static/css/output.css --watch
*/