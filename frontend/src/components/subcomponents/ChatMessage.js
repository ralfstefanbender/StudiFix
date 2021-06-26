import { Button, Card} from '@material-ui/core'
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
            <div>
                {this.state.user.firstname} : <Card variant='outlined' style={{backgroundColor:"#90EE90"}}>{this.state.chatMessage.text}</Card> {this.state.chatMessage.creation_date}
                <Button size="small" onClick={() => this.props.deleteChatMessage(this.state.chatMessage.id)}>X</Button>
            </div>
        )
    }
}

export default ChatMessage