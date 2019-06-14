let searchUrl = 'https://en.wikipedia.org/w/api.php?action=opensearch&format=json&search=';
let contentUrl = 'https://en.wikipedia.org/w/api.php?action=query&prop=revisions&rvprop=content&format=json&titles=';

let userInput;

let counter = 0;
var text;
var data;
function setup() {
  noCanvas();
  userInput = select('#userinput');
  userInput.changed(goWiki);
  goWiki();

  function goWiki(){
      let term = userInput.value();
      let url = searchUrl + term;
      loadJSON(url, gotData, 'jsonp');
  }
  function gotData(data){
      data = data;
      console.log(data);
      console.log(data[2]);
      text = data[2][0];
      assign(text);
      
    }
  function assign(text){
      text = text;
  }
}
var t = text;
console.log(t+'helaskdfl;ahsldfh');


document.write(t);