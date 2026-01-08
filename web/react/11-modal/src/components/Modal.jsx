import classes from './Modal.module.css';

// children is a special prop that contains whatever you include between the opening and closing tags when invoking a component

function Modal({ children }) {
    return (
    <>
        <div className={classes.backdrop} />
        <dialog open className={classes.modal}>
            {children}
        </dialog>
    </>
    );
}

export default Modal;