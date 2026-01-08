import { useState } from 'react';

import Post from './Post';
import classes from './PostsList.module.css';
import NewPost from './NewPost';
import Modal from './Modal';

function PostsList() {

    const [enteredBody, setEnteredBody] = useState('');
    const [enteredAuthor, setEnteredAuthor] = useState('');

    function bodyChangeHandler(event) {
        setEnteredBody(event.target.value);
    }
    function authorChangeHandler(event) {
        setEnteredAuthor(event.target.value);
    }

    return (
        <>
            <Modal>
                <NewPost 
                onBodyChange={bodyChangeHandler} 
                onAuthorChange={authorChangeHandler} />
            </Modal>
            <ul className={classes.posts}>
                <Post className={classes.post} author={enteredAuthor} body={enteredBody} />
                <Post className={classes.post} author="Manuel" body="I love programming" />
            </ul>

        </>
    );
}

export default PostsList;