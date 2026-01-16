import { useState } from 'react';

import Post from './Post';
import classes from './PostsList.module.css';
import NewPost from './NewPost';
import Modal from './Modal';

function PostsList({ isPosting, onStopPosting }) {
    const [enteredBody, setEnteredBody] = useState('');
    const [enteredAuthor, setEnteredAuthor] = useState('');

    function bodyChangeHandler(event) {
        setEnteredBody(event.target.value);
    }
    function authorChangeHandler(event) {
        setEnteredAuthor(event.target.value);
    }

    // condition && code; code will be executed only if condition is true

    return (
        <>
            {isPosting && (
                <Modal onClose={onStopPosting}>
                    <NewPost
                        onBodyChange={bodyChangeHandler}
                        onAuthorChange={authorChangeHandler}
                        onCancel={onStopPosting}
                    />
                </Modal>)
            }
            <ul className={classes.posts}>
                <Post className={classes.post} author={enteredAuthor} body={enteredBody} />
                <Post className={classes.post} author="Manuel" body="I love programming" />
            </ul>

        </>
    );
}

export default PostsList;