import React, { Component } from 'react';
import theme from './theme';
import { ThemeProvider } from '@material-ui/core/styles';

class App extends Component {

 render(){
     return (
     <div>
     <ThemeProvider theme={theme}>
           <//insert what you want to test />
     </ThemeProvider>
     </div>

);
}
}

export default App;
