/**
 * Sample React Native App
 * https://github.com/facebook/react-native
 * @flow
 */

import React, { Component } from 'react';
import {
  Platform,
  StyleSheet,
  Text,
  View,
  Dimensions
} from 'react-native';

import { CameraRoll } from 'react-native';

import Camera from 'react-native-camera';

import { RNS3 } from 'react-native-aws3';




type Props = {};
export default class App extends Component<Props> {





  takePicture() {
     this.camera.capture()
        .then((data) => {
           console.log(data)
           PicturePath = data.path;
          console.log('Path ------------------------------- '+ PicturePath);

          const file = {
            // `uri` can also be a file system path (i.e. file://)
            uri: PicturePath,
            name: "documentVision.jpg",
            type: "image/jpg"
          }

          const options = {
          keyPrefix: "uploads/",
          bucket: "bitbucket18",
          region: "us-east-1",
          accessKey: "AKIAJ556MMZJIRAHQNBQ",
          secretKey: "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",
          successActionStatus: 201
        }


        console.log("DONEEEEEEEEEEEEEEEEEEEEEEEEE")
        RNS3.put(file, options).then(response => {
        if (response.status !== 201)
          throw new Error("Failed to upload image to S3");
        console.log("RESPONSEEEEEEE-----------------"+response.body);
        
      });



  })
}



  render() {
    return (
      <Camera
     ref={(cam) => {
         this.camera = cam;
      }}
      style={styles.preview}
      aspect={Camera.constants.Aspect.fill}>
         <Text style={styles.capture} onPress={
           setInterval(this.takePicture.bind(this), 3000)


         }>



            [CAPTURE]
         </Text>
  </Camera>
    );
  }

}



const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    backgroundColor: '#F5FCFF',
  },
  welcome: {
    fontSize: 20,
    textAlign: 'center',
    margin: 10,
  },
  instructions: {
    textAlign: 'center',
    color: '#333333',
    marginBottom: 5,
  },
  preview: {
   flex: 1,
   justifyContent: 'flex-end',
   alignItems: 'center',
  //  height: Dimensions.get('window').height - 100,
  //  width: Dimensions.get('window').width - 100
},
capture: {
   flex: 0,
   backgroundColor: '#fff',
   borderRadius: 5,
   color: '#000',
   padding: 10,
   margin: 40
}
});
