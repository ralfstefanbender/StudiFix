import React, { Component } from 'react'
import { TextField, Button, Card, Typography } from '@material-ui/core'
import { StudyFixAPI } from '../../api'

import { ChatMessageBO } from '../../api'
import GroupChatMessage from './GroupChatMessage'

class GroupChatWindow extends Component {
    constructor(props){
        super(props)

        this.state = {
            currentUser: this.props.currentUser,
            groupUserBOs: null,
            groupchat: this.props.groupchat,
            groupChatMessages: null,
            newMessage: null
        }
    }

    componentDidMount(){
        this.getGroupUserBOInChat()
        this.getChatMessages()
    }

    getGroupUserBOInChat(){
        StudyFixAPI.getAPI().getGroupUsersByGroupId(this.state.groupchat.id).then((users) => this.setState({groupUserBOs:users}))
    }

    getChatMessages(){
        StudyFixAPI.getAPI().getChatMessageByChatId(this.state.groupchat.chat_id).then((messages) => this.setState({groupChatMessages:messages}))
    }

    deleteChatMessage = (id) => {
        this.setState({groupChatMessages:this.state.groupChatMessages.filter(message => message.id != id)})
        StudyFixAPI.getAPI().deleteChatMessage(id)
    }

    handleMessageChange(e){
        if(e.target.value.length <= 200){this.setState({newMessage:e.target.value})}

    }

    sendChatMessage(){
        if(this.state.newMessage){
            const message = new ChatMessageBO()
            message.setChatId(this.state.chat.id)
            message.setUserId(this.state.currentUser.id)
            message.setText(this.state.newMessage)
            StudyFixAPI.getAPI().addChatMessage(message)
            this.setState({
                chatMessages:this.state.chatMessages.concat(message),
                newMessage:""
            })
        } else {
            // leerer Nachricht Errorhandling
            console.log("Keine Nachricht gegeben")
        }
    }

    render() {
        return (
            <Card variant='outlined'>
                <Card variant='outlined'>
                <Typography variant='h6' style={{textAlign:"center"}}>Current Chat:</Typography>
                <Typography variant='h5' style={{textAlign:"center"}}>{this.state.groupchat.name}</Typography>
                </Card>

                <div style={{maxHeight:"50vh", minHeight:"50vh", overflowY: 'scroll'}}>
                    {this.state.groupChatMessages?
                        this.state.groupChatMessages.map((chatMessage) =>
                            <GroupChatMessage key={chatMessage.id} user={this.state.groupUserBOs.concat(this.state.currentUser).filter((user) => user.id == chatMessage.user_id)} chatMessage={chatMessage} deleteChatMessage={this.deleteChatMessage}/>
                        )
                    : null}
                </div>
                <div style={{display:"flex", flexDirection:"row", bottom:"0px"}}>
                    <TextField
                        value={this.state.newMessage}
                        id="outlined-full-width"
                        placeholder="Type a message"
                        fullWidth
                        margin="normal"
                        InputLabelProps={{
                            shrink: true,
                        }}
                        variant="outlined"
                        onChange={(e) => this.handleMessageChange(e)}
                    />
                    <div style={{alignSelf:"center"}}>
                        <Button color="secondary" variant='contained' onClick={() => this.sendChatMessage()}>
                            Send
                        </Button>
                    </div>
                </div>
            </Card>
        )
    }
}

export default GroupChatWindow