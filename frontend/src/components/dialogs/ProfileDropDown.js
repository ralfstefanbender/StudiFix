import React, { Component, createRef } from 'react';
import PropTypes from 'prop-types';
import { Popover, IconButton, Avatar, ClickAwayListener, withStyles, Typography, Paper, Button, Grid, Divider } from '@material-ui/core';
import firebase from 'firebase/app';

/**
 * Zeigt das Profil an und gibt dem User die Möglichkeit sich auszuloggen.
 *
 */
class ProfileDropDown extends Component {

  // a refernce to the avatar button
  #avatarButtonRef = createRef();

  constructor(props) {
    super(props);

    // Init the state
    this.state = {
      open: false,
    }
  }

  /** Drücken des Avatars */
  handleAvatarButtonClick = () => {
    this.setState({
      open: !this.state.open
    });
  }

  /** 
   * Schließen beim Klicken in ein anderes Feld
   */
  handleClose = () => {
    this.setState({
      open: false
    });
  }

  /** 
	 * Ausloggen wenn man Authentifiziert ist.
	 */
  handleSignOutButtonClicked = () => {
    firebase.auth().signOut();
  }

  /** Rendert die Komponente */
  render() {
    const { classes, user } = this.props;
    const { open } = this.state;

    return (
      user ?
        <div>
          <IconButton className={classes.avatarButton} ref={this.#avatarButtonRef} onClick={this.handleAvatarButtonClick}>
            <Avatar src={user.photoURL} />
          </IconButton>

          <Popover open={open} anchorEl={this.#avatarButtonRef.current} onClose={this.handleClose}
            anchorOrigin={{
              vertical: 'top',
              horizontal: 'left',
            }}
            transformOrigin={{
              vertical: 'top',
              horizontal: 'right',
            }}>
            <ClickAwayListener onClickAway={this.handleClose}>
              <Paper className={classes.profileBox}>
                <Typography align='center'>Hello</Typography>
                <Divider className={classes.divider} />
                <Typography align='center' variant='body2'>{user.displayName}</Typography>
                <Typography align='center' variant='body2'>{user.email}</Typography>
                <Divider className={classes.divider} />
                <Grid container justify='center'>
                  <Grid item>
                    <Button color='primary' onClick={this.handleSignOutButtonClicked}>Logout</Button>
                  </Grid>
                </Grid>
              </Paper>
            </ClickAwayListener>
          </Popover>
        </div>
        : null
    )
  }
}

/** Style der Komponente */
const styles = theme => ({
  avatarButton: {
    float: 'right'
  },
  divider: {
    margin: theme.spacing(1),
  },
  profileBox: {
    padding: theme.spacing(1),
    background: theme.palette.background.default,
  }
});

/** PropTypes */
ProfileDropDown.propTypes = {
  /** @ignore */
  classes: PropTypes.object.isRequired,
  /** Eingeloggte Person */
  user: PropTypes.object,
}

export default withStyles(styles)(ProfileDropDown)
