/**npm startimport { makeStyles, Paper, Typography, Link } from '@material-ui/core';
import React, { useEffect, useState } from 'react';
import { StreamChat } from 'stream-chat';
import { Chat, Channel, ChannelHeader, ChannelList, LoadingIndicator, MessageInput, MessageList, Thread, Window } from 'stream-chat-react';

import 'stream-chat-react/dist/css/index.css';

const userToken = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoic3RpbGwtbGltaXQtMiJ9.bEI6suIAePkW_T0gZAUx9MOvxsTyTYtwml8paKuTFVw';

const filters = { type: 'messaging', members: { $in: ['still-limit-2'] } };
const sort = { last_message_at: -1 };

const ManageChat = () => {
  const [chatClient, setChatClient] = useState(null);

  useEffect(() => {
    const initChat = async () => {
      const client = StreamChat.getInstance('y7b99zy467pb');

      await client.connectUser(
        {
          id: 'still-limit-2',
          name: 'still-limit-2',
          image: 'https://getstream.io/random_png/?id=still-limit-2&name=still-limit-2',
        },
        userToken,
      );

      setChatClient(client);
    };

    initChat();
  }, []);

  if (!chatClient) {
    return <LoadingIndicator />;
  }

  return (
    <Chat client={chatClient} theme='messaging light'>
      <ChannelList filters={filters} sort={sort} />
      <Channel>
        <Window>
          <ChannelHeader />
          <MessageList />
          <MessageInput />
        </Window>
        <Thread />
      </Channel>
    </Chat>
  );
};

export default ManageChat;**/

