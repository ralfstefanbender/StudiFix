import CreateStudyGroup from './components/CreateStudyGroup';
import React, { Component } from 'react';
import { ThemeProvider } from '@material-ui/core/styles';
import theme from './theme';

class App extends React.Component {

 render(){
     return (
     <div>
     <ThemeProvider theme={theme}>
           <CreateStudyGroup />
     </ThemeProvider>
     </div>

);
}
}

export default App;