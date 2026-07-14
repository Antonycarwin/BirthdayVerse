const emojis = [
    "🎁",
    "✨",
    "🌟",
    "💜",
    "🎂",
    "🎉"
];

let lastTime = 0;

document.addEventListener(
    "mousemove",
    function(e){

        let now = Date.now();

        if(now - lastTime < 150){
            return;
        }

        lastTime = now;


        let particle = document.createElement("div");


        particle.innerHTML =
        emojis[
            Math.floor(
                Math.random() * emojis.length
            )
        ];


        particle.style.position = "fixed";

        particle.style.left =
        e.clientX + "px";

        particle.style.top =
        e.clientY + "px";


        particle.style.pointerEvents =
        "none";


        particle.style.fontSize =
        "16px";


        particle.style.zIndex =
        "9999";


        particle.style.filter =
        "drop-shadow(0 0 8px #c084fc)";


        particle.style.transition =
        "all 0.8s ease";


        document.body.appendChild(
            particle
        );


        setTimeout(function(){

            particle.style.transform =
            "translateY(-35px) scale(1.4)";

            particle.style.opacity =
            "0";

        },50);



        setTimeout(function(){

            particle.remove();

        },900);


    }
);