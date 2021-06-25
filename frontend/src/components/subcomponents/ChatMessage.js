import { Button, ButtonGroup} from '@material-ui/core'
import React, { Component } from 'react'

class ChatMessage extends Component {
    constructor(props){
        super(props)

        this.state = {
            user: this.props.user[0],
            chatMessage: this.props.chatMessage
        }
    }

    render() {
        
        return (
            <div style={{backgroundColor:"lightblue", margin:"10px 5px"}}>
                {this.state.user.firstname} : {this.state.chatMessage.text} {this.state.chatMessage.creation_date}
                <Button size="small" onClick={() => this.props.deleteChatMessage(this.state.chatMessage.id)}>X</Button>
            </div>
        )
    }
}

export default ChatMessage