import Post from './Post';
import classes from './PostsList.module.css';
import NewPost from './NewPost';
import Modal from './Modal';

function PostsList({ isPosting, onStopPosting }) {
    // condition && code; code will be executed only if condition is true

    return (
        <>
            {isPosting && (
                <Modal onClose={onStopPosting}>
                    <NewPost
                        onCancel={onStopPosting}
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