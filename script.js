document.addEventListener('DOMContentLoaded', function () {
    // element-one: Dupla kattintásra hozzáad egy "animation" class-t kattintáskor
    const elementOne = document.getElementById('element-one');
    elementOne.ondblclick=function(event){
        event.preventDefault=false;
        elementOne.classList.add("animation")
    }

    // element-two: Ha rámegy az egér, hozzáad egy box-shadow-t
    const elementTwo = document.getElementById('element-two');
    elementTwo.onmouseover=function(event){
        event.preventDefault=false;
        elementTwo.style.boxShadow = "5px 10px #888"
    }
    

    // element-three: Kattintásra eltűnik
    const elementThree = document.getElementById('element-three');
    elementThree.onclick= function(event){
        event.preventDefault=false;
        elementTwo.classList.add("hidden")
    }

    // element-four: Kattintásra a háttere zöld lesz
    const elementFour = document.getElementById('element-four');
    elementFour.onclick=function(event){
        event.preventDefault=false;
        elementFour.style.backgroundColor="green"
    }
    
});