import React, { Component } from 'react'
import { Card, Typography } from '@material-ui/core';

import { List, Button} from '@material-ui/core';

//**Chat auflistung für Gruppenchats Component */
class GroupChatSelection extends Component {

  constructor(props){
    super(props);

    this.state = {
      activeGroupChats: this.props.groupchats
    }
  }

  render(){

    //** Rendern aller Gruppenchats die der Nutzer hat */
    return (
      <div elevation={0}>
        <div >
          <Card variant='outlined'>
          <Typography variant='h6' style={{textAlign:"center"}}>
            Meine Gruppenchats
          </Typography>
          </Card>
          <Card variant='outlined'>
          <List  style={{display:"flex", flexDirection:"column"}}>
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

export default GroupChatSelection;