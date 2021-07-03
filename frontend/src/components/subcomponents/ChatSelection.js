import React, { Component } from 'react'
import { Card, Typography } from '@material-ui/core';

import { List, Button} from '@material-ui/core';

class ChatSelection extends Component {

  constructor(props){
    super(props);

    this.state = {
      activeChats: this.props.chats,
    }
  }

  render(){

    return (
      <div elevation={0}>
        <div>
          <Card variant='outlined'>
          <Typography variant='h6' style={{textAlign:"center"}}>
            Meine Chats
          </Typography>
          </Card>
          <Card variant='outlined'>
          <List style={{display:"flex", flexDirection:"column"}}>
            {this.state.activeChats?
                this.state.activeChats.map((chat)=>{
                    return(
                    
                      <Button variant='outlined' color='secondary' style={{width:"100%"}} key={chat.id} onClick={() => this.props.setSelectedChat(chat)}>
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


export default ChatSelection;