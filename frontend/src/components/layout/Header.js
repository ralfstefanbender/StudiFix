import React, { Component } from 'react';
import { Avatar,
  Button,
  Grid,
  withStyles,
  AppBar,
  Toolbar,
  Typography,
  IconButton,
  Menu,
  MenuItem,
  Box} from '@material-ui/core';
import MenuIcon from '@material-ui/icons/Menu';
import PersonIcon from '@material-ui/icons/Person';
//import firebase from 'firebase/app';


class Header extends Component {
  constructor(props){
    super(props)
    this.state={
      auth: true,
      anchorEl: null,
      mobileAnchorEl: null,
    }

  }

  navigateProfile = () => {
    this.props.history.push({
      pathname: '/profile',
      state: {
        cUser: this.props.history.location.state.cUser
      }
    })
  }

  navigateHome = () => {
    this.props.history.push({
      pathname: '/home',
      state: {
        cUser: this.props.history.location.state.cUser
      }
    })
  }


  navigateChat = () => {
    this.props.history.push({
      pathname: '/chat',
      state: {
        cUser: this.props.history.location.state.cUser
      }
    })
  }

   navigateLerngruppen = () => {
    this.props.history.push({
      pathname: '/studygroup',
      state: {
        cUser: this.props.history.location.state.cUser
      }
    })
  }

   navigateLernpartner = () => {
    this.props.history.push({
      pathname: '/lernpartner',
      state: {
        cUser: this.props.history.location.state.cUser
      }
    })
  }


  handleMobileMenu = (event) => {
    this.setState({
      mobileAnchorEl: event.currentTarget,
    })
  }

  handleMobileClose = () => {
    this.setState({
      mobileAnchorEl: null
    })
  }

  //handleSignOutButtonClicked = () => {
  //  firebase.auth().signOut();
  // }

  onClickAbout = () => {
      this.props.history.push({
            pathname:"/about",
            state: {
              cUser: this.props.history.location.state.cUser
            }
        })
  }

  render() {
    const { classes } = this.props;
    return (

      <div >
        <AppBar position="fixed">
          <Toolbar>
            <Typography variant='h3' component='h1' align='center'>
            HdM Bank Administration
            </Typography>

            <Typography className={classes.header} style={{ fontSize: 25 }}>
            StudyFix
            </Typography>
            <Box display={{xs:"none", sm:"none", md:"block"}}  justify="center" alignItems="center">
            <Button color="inherit" onClick={this.navigateHome}>
              Home
            </Button>

            <Button color="inherit"  onClick={this.navigateProfile} >
              Dein Profil
            </Button>

            <Button color="inherit" onClick={this.navigateChat} >
              Chat
            </Button>

             <Button color="inherit" onClick={this.navigateStudyGroup} >
              Lerngruppen
            </Button>

            <Button color="inherit" onClick={this.navigateLernpartner}  >
              Lernpartner
            </Button>
            <PersonIcon variant="square" className={classes.logo}/>

            <Button color="inherit" onClick={this.onClickAbout}>
              About
            </Button>
            <Button color="inherit" onClick={this.handleSignOutButtonClicked}>
              Logout
            </Button>
            </Box>
            <Box display={{xs:"block", sm:"block", md:"none"}}>
            <PersonIcon
              aria-label="account of current user"
              aria-controls="menu-appbar"
              aria-haspopup="true"
              onClick={this.handleMobileMenu}
              color="inherit"
            >
              <MenuIcon />
            </PersonIcon>
            <Menu
              id="menu-appbar"
              anchorEl={this.state.mobileAnchorEl}
              keepMounted
              open={Boolean(this.state.mobileAnchorEl)}
              onClose={this.handleMobileClose}
            >
              <MenuItem onClick={() => {this.navigateHome(); this.handleMobileClose()}}>Home</MenuItem>
              <MenuItem onClick={() => {this.navigateProfile(); this.handleMobileClose()}}>Profile</MenuItem>
               <MenuItem onClick={() => {this.navigateChat(); this.handleMobileClose()}}>Chat</MenuItem>
               <MenuItem onClick={() => {this.navigateLerngruppen(); this.handleMobileClose()}}>Lerngruppen</MenuItem>
               <MenuItem onClick={() => {this.navigateLernpartner(); this.handleMobileClose()}}>Lernpartner</MenuItem>
              <MenuItem onClick={() => {this.onClickAbout(); this.handleMobileClose()}}>About</MenuItem>
              <MenuItem onClick={() => {this.handleSignOutButtonClicked(); this.handleMobileClose()}}>Logout</MenuItem>
            </Menu>
            </Box>
          </Toolbar>
        </AppBar>
      </div>
    );
  }
}

const styles = theme => ({
  root:{
    flexGrow: 1,
  },
  logo:{
    marginRight: theme.spacing(2)
  },
  header:{
    flexGrow: 1,
  }
});

export default withStyles(styles)(Header);
