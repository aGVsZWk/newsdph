import React, { Component } from 'react';
import ReactPlayer from 'react-player'
import '@/css/player.less'

/**
 * ffmpeg -i xuexingaiqinggushi.mkv -hls_time 10 -hls_list_size 0 -hls_segment_filename ./hls/xuexingaiqinggushi_%05d.ts ./hls/xuexingaiqinggushi.m3u8
 */


class VideoPlay extends Component {
  constructor(props) {
    super(props);
    this.state = {
    }
  }
  render() {
    return (
      <div className="player">
        {/* <ReactPlayer url='https://www.youtube.com/watch?v=HgzGwKwLmgM' controls playing volume={0.8} width={'100%'} height={'100%'} /> */}
        {/* <ReactPlayer url='/media/videos/xuexingaiqinggushi.mkv' controls playing volume={0.8} width={'100%'} height={'100%'} /> */}
        <ReactPlayer url='/media/videos/hls/xuexingaiqinggushi.m3u8' controls playing volume={0.8} width={'100%'} height={'100%'} config={{
          file: {
            forceHLS: true,
          }
        }} />
        {/* <ReactPlayer
          url={[
            'https://www.youtube.com/watch?v=oUFJJNQGwhk',
            'https://www.youtube.com/watch?v=jNgP6d9HraI'
          ]}
        /> */}

      </div>
    );
  }

}

export default VideoPlay;
