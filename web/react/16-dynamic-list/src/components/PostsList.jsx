import { useState } from 'react';
import Post from './Post';
import classes from './PostsList.module.css';
import NewPost from './NewPost';
import Modal from './Modal';

function PostsList({ isPosting, onStopPosting }) {

    // list of posts
    const [posts, setPosts] = useState([]);
    function addPostHandler(postData) {
        
        // spread operator ("...") to add the new post
        // not a good way to do it below
        // setPosts([postData, ...posts]);
        
        // better way to update the state:
        setPosts((existingPosts) => [postData, ...existingPosts]);
        // this way is more reliable when the state update
    }

    return (
        <>
            {isPosting && (
                <Modal onClose={onStopPosting}>
                    <NewPost
                        onCancel={onStopPosting}
                        onAddPost={addPostHandler}
                    />
                </Modal>)
            }
            <ul className={classes.posts}>
                <Post className={classes.post} author="Manuel" body="I love programming" />
            </ul>

        </>
    );
}

export default PostsList;