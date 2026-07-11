const input = document.querySelector("input");

if(input){
    input.focus();

    input.addEventListener("input", function(){
        this.value = this.value.toLowerCase();
    });
}