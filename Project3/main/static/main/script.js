// Get the root element
var r = document.querySelector(':root');

// Create a function for setting a variable value
function myFunction_set(fruit, vegetable, grain, protein, dairy, sodium, sat_fat) {
  // Set the value of variable --blue to another value (in this case "lightblue")
  r.style.setProperty('--fruit', fruit+'deg');
  r.style.setProperty('--vegetable', fruit+'deg '+vegetable+'deg');
  r.style.setProperty('--grain', vegetable+'deg '+grain+'deg');
  r.style.setProperty('--protein', grain+'deg '+protein+'deg');
  r.style.setProperty('--dairy', protein+'deg '+dairy+'deg');
  r.style.setProperty('--sodium', dairy+'deg '+sodium+'deg');
  r.style.setProperty('--saturated_fat', sodium+'deg '+sat_fat+'deg');
  r.style.setProperty('--sugar', '0');
}

function analyzeDiet(breakfast, lunch, dinner, snacks)
{
    document.diet_form.action = "/analyze_diet"; 
    alert(documetn.user_form.action); 
    return false; 
}