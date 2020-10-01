# -*- coding: utf-8 -*-
import asyncio

async def run_postproccessing():
    print('Launching Flask API...')
    flask_process = await asyncio.create_subprocess_exec('python', '-m', 'api')
    flask_return_code = await flask_process.wait()
    print(f'Flask API exited with code: {flask_return_code}')

async def run_web_client():
    print('Launching Svelte pages...')
    npm_process = await asyncio.create_subprocess_exec('npm', 'run', 'dev')
    npm_return_code = await npm_process.wait()
    print(f'Svelte pages exited with code: {npm_return_code}')

if __name__ == "__main__":
    tasks = [
        asyncio.ensure_future(run_postproccessing()),
        asyncio.ensure_future(run_web_client()),
    ]

    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.gather(*tasks))
    loop.close()