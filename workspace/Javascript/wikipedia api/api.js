    let searchUrl = 'https://en.wikipedia.org/w/api.php?action=opensearch&format=json&search=';
    let contentUrl = 'https://en.wikipedia.org/w/api.php?action=query&prop=revisions&rvprop=content&format=json&titles=';

    let userInput;

    let counter = 0;
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
          for (let i = 0 ; i < data[2].length ; i++){
          createP(toPreferred(data[2][i])); 
          }
          
      }
      function toPreferred(text){
        for(let i = 0; i<text.length ; i++){
            if(text[i] === '[' || text[i] === "]" || text[i] === '(' || text[i] === ')' || !isNaN(text[i])){
                text = text.replace(text[i], " ");
            }

            
        }        
        return text;
      }
    }