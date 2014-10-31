# ------------------------------------------------------------------------------
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#  http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#
#  See the License for the specific language governing permissions and
#  limitations under the License.
# ------------------------------------------------------------------------------
"""
The interfaces used by the various station types as well as the hardware
abstractions.
"""

from abc import ABCMeta
from abc import abstractmethod
from abc import abstractproperty
import logging
import logging.handlers


# ------------------------------------------------------------------------------
class IConnectionManager:
    """
    TODO class comment
    """
    __metaclass__ = ABCMeta

    # --------------------------------------------------------------------------
    @abstractmethod
    def run(self):
        """TODO strictly one-line summary

        TODO Detailed multi-line description if
        necessary.

        Args:
            arg1 (type1): TODO describe arg, valid values, etc.
            arg2 (type2): TODO describe arg, valid values, etc.
            arg3 (type3): TODO describe arg, valid values, etc.
        Returns:
            TODO describe the return type and details
        Raises:
            TodoError1: if TODO.
            TodoError2: if TODO.

        """
        pass

    # --------------------------------------------------------------------------
    @abstractmethod
    def startListening(self):
        """TODO strictly one-line summary

        TODO Detailed multi-line description if
        necessary.

        Args:
            arg1 (type1): TODO describe arg, valid values, etc.
            arg2 (type2): TODO describe arg, valid values, etc.
            arg3 (type3): TODO describe arg, valid values, etc.
        Returns:
            TODO describe the return type and details
        Raises:
            TodoError1: if TODO.
            TodoError2: if TODO.

        """
        pass

    # --------------------------------------------------------------------------
    @abstractmethod
    def stopListening(self):
        """TODO strictly one-line summary

        TODO Detailed multi-line description if
        necessary.

        Args:
            arg1 (type1): TODO describe arg, valid values, etc.
            arg2 (type2): TODO describe arg, valid values, etc.
            arg3 (type3): TODO describe arg, valid values, etc.
        Returns:
            TODO describe the return type and details
        Raises:
            TodoError1: if TODO.
            TodoError2: if TODO.

        """
        pass


# ------------------------------------------------------------------------------
class IDisplay:
    """
    Represents an LCD display.
    """
    __metaclass__ = ABCMeta

    # --------------------------------------------------------------------------
    @abstractmethod
    def setLine1Text(self,
                     text):
        """Sets the text for line 1 of the display.

        Sets the text for line 1 of the display. If the text is too long to fit
        on the display, then the text scrolls over time.

        Args:
            text (string): The text to display.
        Returns:
            N/A.
        Raises:
            N/A.

        """
        pass


    # --------------------------------------------------------------------------
    @abstractmethod
    def setLine2Text(self,
                     text):
        """Sets the text for line 2 of the display.

        Sets the text for line 2 of the display. If the text is too long to fit
        on the display, then the text scrolls over time.

        Args:
            text (string): The text to display.
        Returns:
            N/A.
        Raises:
            N/A.

        """
        pass


    # --------------------------------------------------------------------------
    @abstractmethod
    def setText(self,
                text):
        """Sets the text for the entire display.

        Directly sets the text for the display. Multiple lines can be provided
        at once by separating with a '\n' character.

        Args:
            text (string): The text to display.
        Returns:
            N/A.
        Raises:
            N/A.

        """
        pass


# ------------------------------------------------------------------------------
class ILed:
    """
    Represents a single light emitting diode.
    """
    __metaclass__ = ABCMeta

    # --------------------------------------------------------------------------
    @abstractmethod
    def turnOff(self):
        """Ceases any illumination of the LED.

        Args:
        Returns:
            N/A.
        Raises:
            N/A.

        """
        pass

    # --------------------------------------------------------------------------
    @abstractmethod
    def turnOn(self):
        """Steadily illuminates the LED.

        Args:
            N/A.
        Returns:
            N/A.
        Raises:
            N/A.

        """
        pass

    # --------------------------------------------------------------------------
    @abstractmethod
    def setFlashing(self):
        """Flashes the LED at a pre-defined period.


        Indefinitely flashes the LED on and off. Configuration of the on/off
        is left up to the implementation.

        Args:
            N/A.
        Returns:
            N/A.
        Raises:
            N/A.

        """
        pass


# ------------------------------------------------------------------------------
class IPushButtonMonitor:
    """
    TODO class comment
    """
    __metaclass__ = ABCMeta

    # --------------------------------------------------------------------------
    @abstractmethod
    def startListening(self):
        """TODO strictly one-line summary

        TODO Detailed multi-line description if
        necessary.

        Args:
            arg1 (type1): TODO describe arg, valid values, etc.
            arg2 (type2): TODO describe arg, valid values, etc.
            arg3 (type3): TODO describe arg, valid values, etc.
        Returns:
            TODO describe the return type and details
        Raises:
            TodoError1: if TODO.
            TodoError2: if TODO.

        """
        pass

    # --------------------------------------------------------------------------
    @abstractmethod
    def stopListening(self):
        """TODO strictly one-line summary

        TODO Detailed multi-line description if
        necessary.

        Args:
            arg1 (type1): TODO describe arg, valid values, etc.
            arg2 (type2): TODO describe arg, valid values, etc.
            arg3 (type3): TODO describe arg, valid values, etc.
        Returns:
            TODO describe the return type and details
        Raises:
            TodoError1: if TODO.
            TodoError2: if TODO.

        """
        pass

    # --------------------------------------------------------------------------
    @abstractmethod
    def registerPushButton(self,
                           name,
                           buttonPressHandler,
                           config):
        """TODO strictly one-line summary

        TODO Detailed multi-line description if
        necessary.

        Args:
            arg1 (type1): TODO describe arg, valid values, etc.
            arg2 (type2): TODO describe arg, valid values, etc.
            arg3 (type3): TODO describe arg, valid values, etc.
        Returns:
            TODO describe the return type and details
        Raises:
            TodoError1: if TODO.
            TodoError2: if TODO.

        """
        pass


# ------------------------------------------------------------------------------
class IStation:
    """
    Represents a specific Raspberry Pi challenge station type.
    """
    __metaclass__ = ABCMeta

    # --------------------------------------------------------------------------
    @abstractproperty
    def stationTypeId(self):
        """The station type identifier passed to the MS.

        The station type identifier that is provided to the MS upon join.

        Args:
            N/A.
        Returns:
            N/A.
        Raises:
            N/A.

        """
        pass

    # --------------------------------------------------------------------------
    @abstractmethod
    def start(self):
        """Performs any processing necessary when the application starts.

        Args:
            N/A.
        Returns:
            N/A.
        Raises:
            N/A.

        """
        pass

    # --------------------------------------------------------------------------
    @abstractmethod
    def stop(self, signal):
        """Performs any clean-up necessary as the application terminates.

        Args:
            signal (int): The number of the signal being handled.
        Returns:
            N/A.
        Raises:
            N/A.

        """
        pass

    # --------------------------------------------------------------------------
    @abstractmethod
    def onReady(self):
        """Prepares the station for the next challenge.

        This is called on station start-up as well as after the previous run
        completes. It should set the station to visually indicate that a user
        may approach and begin the challenge.

        Args:
            N/A.
        Returns:
            N/A.
        Raises:
            N/A.

        """
        pass

    # --------------------------------------------------------------------------
    @abstractmethod
    def onProcessing(self):
        """Begins running the challenge.

        This is called when the MS informs the station that it is time to begin
        the challenge. It follows the user scanning the QR code next to the
        station.

        Args:
            N/A.
        Returns:
            N/A.
        Raises:
            N/A.

        """
        pass

    # --------------------------------------------------------------------------
    @abstractmethod
    def onFailed(self):
        """Completes the challenge with a failed indication.

        This is called when the MS informs the station that the user has failed
        completing the challenge. It should set the station to visually and
        perhaps aurally indicate that the challenge was unsuccessful.

        Args:
            N/A.
        Returns:
            N/A.
        Raises:
            N/A.

        """
        pass

    # --------------------------------------------------------------------------
    @abstractmethod
    def onPassed(self):
        """Completes the challenge with a success indication.

        This is called when the MS informs the station that the user has passed
        completing the challenge. It should set the station to visually and
        perhaps aurally indicate that the challenge was successful.

        Args:
            N/A.
        Returns:
            N/A.
        Raises:
            N/A.

        """
        pass

    # --------------------------------------------------------------------------
    @abstractmethod
    def onUnexpectedState(self, value):
        """Indicates a logic error in the application.

        This indicates a transition to an unrecognized or unexpected state. This
        must be logged and should set the station to visually and perhaps
        aurally indicate the condition in order to help troubleshoot during
        testing.

        Args:
            value (State): The attempted state transition value.
        Returns:
            N/A.
        Raises:
            N/A.

        """
        pass


# ------------------------------------------------------------------------------
class IVibrationMotor:
    """
    Represents a single vibration motor.
    """
    __metaclass__ = ABCMeta

    # --------------------------------------------------------------------------
    @abstractmethod
    def start(self):
        """Steadily vibrates the motor.

        Args:
            N/A.
        Returns:
            N/A.
        Raises:
            N/A.

        """
        pass

    # --------------------------------------------------------------------------
    @abstractmethod
    def stop(self):
        """Ceases vibrating the motor.

        Args:
            N/A.
        Returns:
            N/A.
        Raises:
            N/A.

        """
        pass


# ------------------------------------------------------------------------------
# Module Initialization
# ------------------------------------------------------------------------------
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG) # TODO - delete
handler = logging.handlers.SysLogHandler(address = '/dev/log')
logger.addHandler(handler)

