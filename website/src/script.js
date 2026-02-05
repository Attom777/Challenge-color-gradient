/* loop background color transition 2s ease-in-out */
function colorGen(stop) {

  if (stop) clearInterval(interval);

  const colors = ['#FF0000', '#00FF00', '#0000FF', '#FFFF00', '#FF00FF', '#00FFFF', '#000000', '#FFFFFF'];
  let i = 0;
  const interval = setInterval(function() {
    document.body.style.backgroundColor = colors[i];
    i = (i + 1) % colors.length;
    document.body.style.transition = "2s ease-in-out";
  }, 2000);


}

/* Bool gen */
function gen(state) {

  if (state) {
    console.log("> Genération start !");
    colorGen(false);
  } else if (state) {
    console.log("> Genération stop !");
    colorGen(true);
  } else {
    console.log("Error HTML !");
  }

}

/* Toogle function */
noContext = document.getElementById('noContextMenu');

noContext.addEventListener('contextmenu', e => {

  e.preventDefault();
  console.log("> new click ok !");

  document.body.classList.toggle("gen-true");

  isStart = document.body.classList.contains("gen-true") || null;

  gen(isStart);

});
