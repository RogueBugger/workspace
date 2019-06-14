

function toPreferred(text){
    for(let i = 0; i<text.length ; i++){
        if(text[i] === '[' || text[i] === "]" || text[i] === '(' || text[i] === ')' || !isNaN(text[i])){
            text = text.replace(text[i], " ");
            document.write(text[i]);
        }

        
    }
    return text;
}

var text = window.prompt();
text = toPreferred(text);
document.write(text);



