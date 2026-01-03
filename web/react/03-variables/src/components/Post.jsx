const names = ['Maximilian', 'Manuel'];

function Post() {

    // choose a name randomly
    const chosenName = Math.random() > 0.5 ? names[0] : names[1];
    
    return (
    <div>
        {/* display the chosen name */}
        <p>{chosenName}</p>
        <p>React.js is awesome</p>
    </div>
    );
}

// make the function available to 
// be used outside of this file
export default Post;