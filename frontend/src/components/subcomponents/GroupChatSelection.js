import React, { Component } from 'react'
import { makeStyles, withStyles, Card, Typography, FormHelperText, ButtonGroup} from '@material-ui/core';

import { List, Button} from '@material-ui/core';

class GroupChatSelection extends Component {

  constructor(props){
    super(props);

    this.state = {
      activeChats: this.props.chats,
      activeGroupChats: this.props.groupchats
    }
  }

  render(){
    const { classes } = this.props;

    return (
      <div elevation={0} className={classes.root}>
        <div className={classes.content}>
          <Card variant='outlined'>
          <Typography variant='h6' style={{textAlign:"center"}}>
            Meine Gruppenchats
          </Typography>
          </Card>
          <Card variant='outlined'>
          <List className={classes.chatList} style={{display:"flex", flexDirection:"column"}}>
            {this.state.activeGroupChats?
                this.state.activeGroupChats.map((groupchats)=>{
                    return(

                      <Button variant='outlined' color='secondary' style={{width:"100%"}} key={groupchats.id} onClick={() => this.props.setSelectedChat(groupchats)}>
                        {groupchats.name}
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

export default withStyles(styles)(GroupChatSelection);