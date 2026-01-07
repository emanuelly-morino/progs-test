import { useState } from 'react';

import classes from './NewPost.module.css';

function NewPost() {
    
    // modern javascript way of using useState
    const [enteredBody, setEnteredBody] = useState('');
    
    // create a state variable to hold the textarea value
    //const stateData = useState('');
    //const enteredBody = stateData[0]; // current value of the state variable
    //const setEnteredBody = stateData[1]; // state updating function

    // this variable will not be updated when the user types in the textarea
    // let enteredBody = '';

    function changeBodyHandler(event){
        //console.log(event.target.value);
        // line below would not work as expected because enteredBody is not a state variable
        //enteredBody = event.target.value;
        setEnteredBody(event.target.value);
    }

    return (
        <form className={classes.form}>
            <p>
                <label htmlFor="body">Text</label>
                <textarea id="body" required rows="3" onChange={changeBodyHandler}/>
            </p>
            <p>{enteredBody}</p>
            <p>
                <label htmlFor="name">Your name</label>
                <input type="text" id="name" required />
            </p>
        </form>
    );
}
export default NewPost;