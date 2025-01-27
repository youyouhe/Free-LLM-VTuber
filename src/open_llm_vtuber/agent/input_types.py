from dataclasses import dataclass
from enum import Enum
from typing import Dict, List, Optional, Union
import numpy as np


class ImageSource(Enum):
    """Enum for different image sources"""
    CAMERA = "camera"
    SCREEN = "screen"
    CLIPBOARD = "clipboard"
    UPLOAD = "upload"


class TextSource(Enum):
    """Enum for different text sources"""
    INPUT = "input"  # Main user input/transcription
    CLIPBOARD = "clipboard"  # Text from clipboard


@dataclass
class ImageData:
    """
    Represents an image from various sources
    
    Attributes:
        source: Source of the image
        data: Base64 encoded image data or URL
        mime_type: MIME type of the image (e.g., 'image/jpeg', 'image/png')
    """
    source: ImageSource
    data: str  # Base64 encoded or URL
    mime_type: str


@dataclass
class FileData:
    """
    Represents a file uploaded by the user
    
    Attributes:
        name: Original filename
        data: Base64 encoded file data
        mime_type: MIME type of the file
    """
    name: str
    data: str  # Base64 encoded
    mime_type: str


@dataclass
class TextData:
    """
    Represents text data from various sources
    
    Attributes:
        source: Source of the text
        content: The text content
    """
    source: TextSource
    content: str


class BaseInput:
    """Base class for all input types"""
    pass


@dataclass
class BatchInput(BaseInput):
    """
    Input type for batch processing, containing complete transcription and optional media
    
    Attributes:
        texts: Dictionary of text data from different sources
        images: Dictionary of images keyed by unique identifiers
        files: List of files
    """
    texts: Dict[str, TextData]
    images: Optional[Dict[str, ImageData]] = None
    files: Optional[List[FileData]] = None


@dataclass
class StreamInput(BaseInput):
    """
    Input type for real-time streaming data
    
    Attributes:
        audio_chunk: Numpy array containing audio data
        video_frame: Optional video frame data (Base64 encoded)
    """
    audio_chunk: np.ndarray
    video_frame: Optional[str] = None  # Base64 encoded image
