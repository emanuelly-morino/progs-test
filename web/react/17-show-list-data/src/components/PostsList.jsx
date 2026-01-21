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

            {/* conditional rendering,
            considering if there are
            posts or not */}

            {posts.length > 0 && (
                <ul className={classes.posts}>

                    {/* the key property should be an ID in a future version */}

                    {posts.map((post) => (
                        <Post
                            key={post.body}
                            className={classes.post}
                            author={post.author}
                            body={post.body} />
                    ))}
                </ul>
            )}

            {/* no posts? */}
            {posts.length === 0 && (
                <p className={classes.noPosts}>No posts yet.</p>
            )}

        </>
    );
}

export default PostsList;