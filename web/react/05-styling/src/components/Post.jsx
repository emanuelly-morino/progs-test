// we want to import the css module here
import classes from './Post.module.css';

function Post(props) {   
    // use the 'post' class from the imported css
    return (
    <div className={classes.post}>
        <p className={classes.author}>{props.author}</p>
        <p className={classes.text}>{props.body}</p>
    </div>
    );
}

export default Post;