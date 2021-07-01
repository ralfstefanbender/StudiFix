import React, { Component } from 'react';
import PropTypes from 'prop-types';
import { Paper, Typography, Tabs, Tab, Button, AppBar } from '@material-ui/core';
import { Link as RouterLink } from 'react-router-dom';
import firebase from 'firebase/app';
import ProfileDropDown from "../dialogs/ProfileDropDown";


/*
 */
class Header extends Component {

  constructor(props) {
    super(props);

    // Init an empty state
    this.state = {
      tabindex: 0,
    };
  }

  /** Handles onChange events of the Tabs component */
  handleTabChange = (e, newIndex) => {
    // console.log(newValue)
    this.setState({
      tabindex: newIndex
    })
  };

   handleSignOutButtonClicked = () => {
   firebase.auth().signOut();
  }

  /** Renders the component <ProfileDropDown user={user} />     const { user } = this.props;*/
  render() {
    const { user } = this.props;



    return (
      <Paper variant='outlined' >
        <ProfileDropDown user={user} />
        <Typography variant='h3' component='h1' align='center' color="primary">
          StudiFix
        </Typography>
        <Typography variant='h4' component='h2' align='center'>
          Find your perfect learn buddys!
        </Typography> <br></br>
         {
          user ?
            <Tabs indicatorColor='primary' textColor='primary' value={this.state.tabindex} onChange={this.handleTabChange} >
              <Tab label='Home' component={RouterLink} to={`/overview`} />
              <Tab label='Mein Profil' component={RouterLink} to={`/ManageUser`} />
              <Tab label='Chat' component={RouterLink} to={`/chat`} />
              <Tab label='Lerngruppen' component={RouterLink} to={`/studygroup`} />
              <Tab label='Lernpartner' component={RouterLink} to={`/lernpartner`} />
              <Tab label='Matching' component={RouterLink} to={`/matching_page`} />
              <Tab label='About' component={RouterLink} to={`/about`} />
            </Tabs>
            : null
        }
      </Paper>
    )
  }
}

/** PropTypes */
Header.propTypes = {
  /** The logged in firesbase user */
  user: PropTypes.object,
}

export default Header;