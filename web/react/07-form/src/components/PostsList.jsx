import Post from './Post';
import classes from './PostsList.module.css';   
import NewPost from './NewPost';

function PostsList() {

    // below there is an empty component
    // since we cannot have multiple siblings tags
    // in the main return

    /*
    An "empty tag" in React, written as <></>, 
    is the shorthand syntax for a React Fragment.
    It allows you to group a list of children 
    without adding extra nodes to the DOM, 
    which is essential because 
    React components must return a single root element.
    */

    return (        
        <>  {/* ===> The empty tag (or Fragment) *opens* here 

        This comment is at JSX (javascript XML) markup level
        
        JSX (JavaScript XML) is a syntax extension for JavaScript, 
        primarily used with React to describe user interfaces. 
        It allows developers to write HTML-like 
        structures directly inside JavaScript code, 
        making component rendering more intuitive. 
        JSX gets compiled (transpiled) into 
        regular JavaScript function calls 
        (e.g., React.createElement) by tools like Babel.        
        
        */}
        <NewPost />
        <ul className={classes.posts}>
            <Post className={classes.post} author="Maximilian" body="React.js is awesome" />
            <Post className={classes.post} author="Manuel"
                body="I love programming" />
        </ul>
        </> // ===>Here is the *closing tag* of the Fragment

        // This comment is at javascript level
    );
}

export default PostsList;