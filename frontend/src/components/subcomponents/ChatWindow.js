import React, { Component } from 'react'
import { TextField, Button, Card, Typography } from '@material-ui/core'
import { StudyFixAPI } from '../../api'

import { ChatMessageBO } from '../../api'
import ChatMessage from './ChatMessage'

//** Componente für ein Chatfenster (Einzel und Gruppenchats) */
class ChatWindow extends Component {
    intervalID = 0;

    constructor(props){
        super(props)

        this.state = {
            currentUser: this.props.currentUser,
            userBOs: null,
            chat: this.props.chat,
            chatMessages: null,
            newMessage: null,
            autoscroll: true,
            mounted: false
        }
    }

    //** Sobald Component da ist werden User, Chat Messages geholt und die Refresh funktion gestartet */
    componentDidMount(){
        this.getUserBOInChat()
        this.getChatMessages()
        this.refresh()
        this.setState({mounted:true})
    }
    
    //** Wenn aus dem Chat gegangen wird soll der refresh von neuen Nachrichten aufhören */
    componentWillUnmount(){
        clearInterval(this.intervalID);
    }

    //** Alle nutzer des aktuellen Chats in state speichern */
    getUserBOInChat(){
        StudyFixAPI.getAPI().getOtherUserByChatId(this.state.currentUser.id, this.state.chat.id).then((users) => {this.setState({userBOs:users})})
    }

    //** Alle nachrichten des aktuellen Chats in einen state speichern*/
    getChatMessages(){
        StudyFixAPI.getAPI().getChatMessageByChatId(this.state.chat.id).then((messages) => this.setState({chatMessages:messages}),this.updateScroll())
    }

    //** Bei löschung: Nachricht aus state entfernen und in der db löschen*/
    deleteChatMessage = (id) => {
        if(id != 0){this.setState({chatMessages:this.state.chatMessages.filter(message => message.id != id)})
        StudyFixAPI.getAPI().deleteChatMessage(id)}
    }

    //** bei nachrichteingabe check ob unter 200 buchstaben und state update */
    handleMessageChange(e){
        if(e.target.value.length <= 200){this.setState({newMessage:e.target.value})}
    }
    
    //** Nachricht senden: Message zum state hinzufügen, in db speichern und scroll nach unten */
    sendChatMessage(){
        if(this.state.newMessage){
            const message = new ChatMessageBO()
            message.setChatId(this.state.chat.id)
            message.setUserId(this.state.currentUser.id)
            message.setText(this.state.newMessage)
            StudyFixAPI.getAPI().addChatMessage(message)
            this.setState({chatMessages:this.state.chatMessages.concat(message),newMessage:""})
            setTimeout(this.updateScroll(), 500)
        } else {
            // leere Nachricht Errorhandling
            console.log("Keine Nachricht gegeben")
        }  
    }

    //**Refresh für neue Nachrichten alle 5 sek */
    refresh(){
        this.intervalID = setInterval(() => (this.getChatMessages()), 5000)
    }

    //** Nach unten scrollen */
    updateScroll(){
        if (this.state.autoscroll){
        var element = document.getElementById("chat");
        element.scrollTop = element.scrollHeight}
    }

    render() {
        return (
            <>
            <Card variant='outlined'>
                <Card variant='outlined'>
                <Typography variant='h6' style={{textAlign:"center"}}>Aktueller Chat:</Typography>
                <Typography variant='h5' style={{textAlign:"center"}}>{this.state.chat.name}</Typography>
                </Card>
                
                <div id="chat" style={{maxHeight:"50vh", minHeight:"50vh", overflowY: 'scroll', display:"flex", flexDirection:"column"}}>
                    {this.state.chatMessages && this.state.userBOs? 
                        this.state.chatMessages.map((chatMessage) =>
                            <ChatMessage key={chatMessage.id} currUser={this.state.currentUser} user={this.state.userBOs.concat(this.state.currentUser).filter((user) => user.id == chatMessage.user_id)} chatMessage={chatMessage} deleteChatMessage={this.deleteChatMessage}/>
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
            <Button style={{gridColumn:"2/3", width:"40%"}} onClick={() => this.setState({autoscroll : !this.state.autoscroll})}>{this.state.autoscroll? "Autoscroll ausschalten" : "Autoscroll einschalten"}</Button>
            </>
        )
    }
}

export default ChatWindow