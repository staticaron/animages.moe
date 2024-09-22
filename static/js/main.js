function clamp(min, max, value){
    if( value < min ) return min;
    else if( value > max ) return max;
    return value;
}

async function assign_random_background(){

    const response = await fetch("http://localhost/api/assets");

    const assets = await response.json();

    console.log(assets["files"]);
    console.log(assets["files"].length);

    let random_index = clamp( 0, assets["files"].length - 1, Math.floor( Math.random() * assets["files"].length ) );

    console.log(random_index);

    let random_file = assets["files"][ random_index ];

    console.log(random_file["path"]);

    document.body.style.backgroundImage = `url(${random_file["path"]})`;

    console.log(`url(${random_file["path"]})`);
}