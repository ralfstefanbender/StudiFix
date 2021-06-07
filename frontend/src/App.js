import React, { Component } from 'react';
import theme from './theme';
import Headertwo from './Headertwo';
import { ThemeProvider } from '@material-ui/core/styles';

class App extends Component {

 render(){
     return (
     <div>
     <ThemeProvider theme={theme}>
           <Headertwo />
     </ThemeProvider>
     </div>

);
}
}

export default App;
