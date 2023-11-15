import React from 'react';
import { useNavigate } from 'react-router-dom';
import UploadBox from './UploadBox'
import '../index.css'
import { Button, ConfigProvider } from 'antd';


function UploadPage() {
  let navigate = useNavigate();
  return (
    <div className='upload-page'>

      <h1>CSV/Excel Parzer</h1>

      <div className='container'>
        <UploadBox />
      </div>
      <div className='btn-container'>
        <ConfigProvider theme={{
          token: {
            colorPrimary: '#E63946',

          },
        }}>
          <Button type='primary' style={{ margin: '20px' }} onClick={() => { navigate("/profiles") }}>Generate JSON & Update DB</Button>
        </ConfigProvider>
      </div>

    </div>
  )
}

export default UploadPage