import setuptools

setuptools.setup(
    name="robot_hat",
    version="1.0",
    author="Gavin Andres",
    description="An version of robot-hat that sucks less",
    url="https://github.com/gandres42/robot-hat",
    license="LICENSE.txt",
    packages=setuptools.find_packages(),
    install_requires = [
        'smbus2',
        'gpiozero',
        'pyaudio',
        'spidev',
        'pyserial',
        'pillow',
        'pygame>=2.1.2',
        'pigpio',
        'RPi.GPIO'
    ]
)