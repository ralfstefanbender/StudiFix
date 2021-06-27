import { Button, Card} from '@material-ui/core'
import React, { Component } from 'react'

class GroupChatMessage extends Component {
    constructor(props){
        super(props)

        this.state = {
            user: this.props.user[0],
            groupChatMessage: this.props.groupChatMessage
        }
    }

    render() {

        return (
            <div>
                {this.state.user.firstname} : <Card variant='outlined' style={{backgroundColor:"#90EE90"}}>{this.state.groupChatMessage.text}</Card> {this.state.groupChatMessage.creation_date}
                <Button size="small" onClick={() => this.props.deleteChatMessage(this.state.chatMessage.id)}>X</Button>
            </div>
        )
    }
}

export default GroupChatMessage