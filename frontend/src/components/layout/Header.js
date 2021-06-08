import React, { Component } from 'react';
import PropTypes from 'prop-types';
import { Paper, Typography, Tabs, Tab } from '@material-ui/core';
import { Link as RouterLink } from 'react-router-dom';


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

  /** Renders the component <ProfileDropDown user={user} />     const { user } = this.props;*/
  render() {


    return (
      <Paper variant='outlined' >

        <Typography variant='h3' component='h1' align='center'>
          StudyFix
        </Typography>
        <Typography variant='h4' component='h2' align='center'>
          Find your perfect learn buddys!
        </Typography>

            <Tabs indicatorColor='primary' textColor='primary' centered value={this.state.tabindex} onChange={this.handleTabChange} >
            <Tab label='Home' component={RouterLink} to={`/overview`} />
              <Tab label='Mein Profil' component={RouterLink} to={`/user`} />
              <Tab label='Chat' component={RouterLink} to={`/chat`} />
              <Tab label='Lerngruppen' component={RouterLink} to={`/lerngruppen`} />
              <Tab label='Lernpartner' component={RouterLink} to={`/lernpartner`} />
              <Tab label='About' component={RouterLink} to={`/about`} />
            </Tabs>

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