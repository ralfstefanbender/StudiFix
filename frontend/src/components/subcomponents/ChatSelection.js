import React, { Component } from 'react'
import { makeStyles, withStyles, Card, Typography, FormHelperText} from '@material-ui/core';

import { List, Button } from '@material-ui/core';

class ChatSelection extends Component {

  constructor(props){
    super(props);

    this.state = {
      activeChats: this.props.chats
    }
  }

  render(){
    const { classes } = this.props;

    return (
      <div elevation={0} className={classes.root}>
        <div className={classes.content}>
          <Card variant='outlined'>
          <Typography variant='h6' style={{textAlign:"center"}}>
            My Chats
          </Typography>
          </Card>
          <Card variant='outlined'>
          <List className={classes.chatList} style={{display:"flex", flexDirection:"column"}}>
            {this.state.activeChats?
                this.state.activeChats.map((chat)=>{
                    return(
                    <Button style={{width:"100%"}} key={chat.id} onClick={() => this.props.setSelectedChat(chat)}>
                        {chat.name}
                    </Button>
                    )
                })
            :null}
            
          </List>
          </Card>

        </div>
      </div>
    )
  }
}

const styles = makeStyles(theme => ({
  root: {
    width: '30%',
    marginTop: theme.spacing(2),
    marginBottom: theme.spacing(2),
    padding: theme.spacing(1)
  },
  content: {
    margin: theme.spacing(1),
  }
}));

export default withStyles(styles)(ChatSelection);