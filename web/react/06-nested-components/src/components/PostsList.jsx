import Post from './Post';
import classes from './PostsList.module.css';   

function PostsList() {
    return (
        <ul className={classes.posts}>
            <Post className={classes.post} author="Maximilian" body="React.js is awesome" />
            <Post className={classes.post} author="Manuel"
                body="I love programming" />
        </ul>
    );
}

export default PostsList;