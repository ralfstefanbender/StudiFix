import React, { Component } from 'react';
import PropTypes from 'prop-types';
import { Paper, Typography, Tabs, Tab, Button } from '@material-ui/core';
import { Link as RouterLink } from 'react-router-dom';
import firebase from 'firebase/app';


/*
 */
class Header extends Component {

  constructor(props) {
    super(props);

    // Init an empty state
    this.state = {
      tabindex: 0
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

        <Typography variant='h3' component='h1' align='center'>
          StudyFix
        </Typography>
        <Typography variant='h4' component='h2' align='center'>
          Find your perfect learn buddys!
        </Typography>
         {
          user ?

            <Tabs indicatorColor='primary' textColor='primary' centered value={this.state.tabindex} onChange={this.handleTabChange} >
            <Tab label='Homer' component={RouterLink} to={`/overview`} />
              <Tab label='Mein Profil' component={RouterLink} to={`/user`} />
              <Tab label='Chat' component={RouterLink} to={`/chat`} />
              <Tab label='Lerngruppen' component={RouterLink} to={`/lerngruppen`} />
              <Tab label='Lernpartner' component={RouterLink} to={`/lernpartner`} />
              <Tab label='About' component={RouterLink} to={`/about`} />
               <Button color="inherit" onClick={this.handleSignOutButtonClicked}>
              Log out
            </Button>
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