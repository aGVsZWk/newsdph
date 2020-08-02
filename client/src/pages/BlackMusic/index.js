import React, {Component} from "react";
import bus from '@/utils/bus'
import { getSongUrl } from '@/api/discovery';
import Discovery from './Discovery'
import Playlists from './Playlists'

import {
  HashRouter as Router,
  Link,
  Route,
  Switch,
  Redirect,
} from 'react-router-dom'


class BlackMusic extends Component {
	constructor(props) {
		super(props);
    this.state = {
      url: '',
    }
    this.audioRef = React.createRef()
	}
  componentDidMount() {
    // 播放音乐
    bus.on('playMusic', async (id) => {
      const data = await getSongUrl({ id })
      console.log(data);
      if (data.code === 200) {
        this.setState({
          url: data.data[0].url,
        })
      }
    })

    // 暂停音乐
    bus.on('pauseMusic', () => {
      this.audioRef.current.pause()
    })
  }
	render() {
		return (
        <div className="index-container">
          <div className="nav">
            <ul>
              <li>
                <Link activeclassname="router-link-active" to="/music/discovery">
                  <span className="iconfont icon-find-music"></span>
                  发现音乐
                </Link>
              </li>
              <li>
                <Link activeclassname="router-link-active" to="/music/playlists">
                  <span className="iconfont icon-music-list"></span>
                  推荐歌单
                </Link>
              </li>
              <li>
                <Link activeclassname="router-link-active" to="music/songs">
                  <span className="iconfont icon-music"></span>
                  最新音乐
                </Link>
              </li>
              <li>
                <Link activeclassname="router-link-active" to="music/mvs">
                  <span className="iconfont icon-mv"></span>
                  最新MV
                </Link>
              </li>
            </ul>
          </div>
          <div className="main">
            <Switch>
              <Route path="/music/discovery" component={Discovery} />
              <Route path="/music/playlists" component={Playlists} />
            </Switch>
          </div>
          <div className="player">
            <audio
              ref={this.audioRef}
              controls
              autoPlay
              src={this.state.url}
              loop
            ></audio>
          </div>
        </div>
		)
	}
}

export default BlackMusic;
