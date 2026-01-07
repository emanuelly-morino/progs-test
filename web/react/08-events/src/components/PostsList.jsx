import Post from './Post';
import classes from './PostsList.module.css';   
import NewPost from './NewPost';

function PostsList() {
    // below there is an empty component
    // since we cannot have multiple siblings tags
    // in the main return
    return (
        <>
        <NewPost />
        <ul className={classes.posts}>
            <Post className={classes.post} author="Maximilian" body="React.js is awesome" />
            <Post className={classes.post} author="Manuel"
                body="I love programming" />
        </ul>
        </>
    );
}

export default PostsList;